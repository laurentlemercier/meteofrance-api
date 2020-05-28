# -*- coding: utf-8 -*-
"""
Meteo France weather forecast python API.
"""

from requests import Session, Response
from .const import METEOFRANCE_API_URL, METEOFRANCE_API_TOKEN


class Auth:
    """Class to make authenticated requests."""

    def __init__(self, websession: Session, host: str, access_token: str):
        """Initialize the auth."""
        self.websession = websession
        self.host = host
        self.access_token = access_token

    def request(self, method: str, path: str, **kwargs) -> Response:
        """Make a request."""
        params = kwargs.pop("params", None)

        if params is None:
            params = {}
        else:
            params = dict(params)

        params["token"] = self.access_token

        return self.websession.request(
            method, f"{self.host}/{path}", **kwargs, params=params
        )


class AuthMeteofrance(Auth):
    """Generic Auth for meteofrance as token is static."""

    # TODO: convert to class method
    def __init__(self):
        super().__init__(Session(), METEOFRANCE_API_URL, METEOFRANCE_API_TOKEN)