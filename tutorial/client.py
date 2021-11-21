from gql import Client
from gql.transport.requests import RequestsHTTPTransport

transport = RequestsHTTPTransport(url='http://localhost:8080/v1/graphql')

client = Client(transport=transport, fetch_schema_from_transport=True)