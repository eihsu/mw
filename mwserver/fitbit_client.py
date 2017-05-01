# https://dev.fitbit.com/docs/body/#get-weight-logs

import datetime
import json
import requests
from requests_oauthlib import OAuth2Session

class Timeout(Exception):
    pass
class Unauthorized(Exception):
    pass
class BadResponse(Exception):
    pass


class FitbitClient(object):
    """
    Client for retrieving the most recent set of weights for our
    registered fitbit users.
    """

    API_ENDPOINT = "https://api.fitbit.com"
    API_VERSION = 1
    QUERY_PERIOD = '7d' # [1d/7d/30d/1w/1m/3m/6m/1y/max]  
    TIMEOUT_IN_S = 30

    def __create_session(self, user_id, access_token):
        """
        Create an OAuth2 session for given user_id using supplied access_token.
        We don't worry about refreshing tokens, as the ones we generated manually
        using fitbit dev dummy interface (April 2017) will last for one year.
        """
        return OAuth2Session(
            user_id,
            token={'access_token': access_token}
        )


    def __make_request(self, session, url):
        """
        Given an OAuth2 session and a url to hit, make a request for that url
        while throwing exceptions for 202's, 401's, timeouts, and unparseable
        json content.
        """
        try:
            resp = session.request('GET', url, timeout=self.TIMEOUT_IN_S)
            if resp.status_code == 401:
                raise Unauthorized
        except requests.Timeout as e:
            raise Timeout(*e.args)

        if resp.status_code == 202:  # accepted but not processed: no-op
            return True

        try:  # parse json response, throw parsing errors.
            content = json.loads(resp.content.decode('utf8'))
        except ValueError:
            raise BadResponse

        return content


    def get_measurements(self, user_id, access_token):
        """
        Given a Fitbit user id and their access token, create a session
        and use it to request the user's most recent weight measurements.
        Specific query is assembled by counting back a certain period of time
        from the current date.
        """
        session = self.__create_session(user_id, access_token)

        today = datetime.date.today()
        today_string = today.strftime('%Y-%m-%d')
        date_string = today_string + '/' + self.QUERY_PERIOD

        base_url = "{}/{}/user/{}/body/log/weight/date/{}.json"
        url = base_url.format(self.API_ENDPOINT,
                              self.API_VERSION,
                              user_id,
                              date_string)

        return self.__make_request(session, url)
    

