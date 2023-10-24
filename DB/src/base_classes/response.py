


class Response:
    def __init__(self, response: dict):
        self._response = response

    def validate(self, schema):
        if isinstance(self._response, list):
            for item in self._response:
                schema.model_validate(item)
        else:
            schema.model_validate(self._response)
        return self
