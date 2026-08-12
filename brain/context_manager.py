class ContextManager:

    def __init__(self):
        self.user_context = {}

    def set(self, user_id, key, value):
        """
        Store a value for a specific user.
        """

        if user_id not in self.user_context:
            self.user_context[user_id] = {}

        self.user_context[user_id][key] = value

    def get(self, user_id, key):
        """
        Retrieve a value for a specific user.
        """

        if user_id not in self.user_context:
            return None

        return self.user_context[user_id].get(key)

    def clear(self, user_id):
        """
        Remove all stored context for a user.
        """

        if user_id in self.user_context:
            del self.user_context[user_id]

    def get_all(self, user_id):
        """
        Return the complete context of a user.
        """

        if user_id not in self.user_context:
            return {}

        return self.user_context[user_id]