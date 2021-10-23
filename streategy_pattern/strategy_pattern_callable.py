import uuid


class CustomerSupport(object):

    def __init__(self, ticket_id: str, issue: str):
        self.ticket_id = ticket_id
        self.issue: str = issue

    def process_tickets(self):
        pass