class RequestViewMixin:
    def get_form_kwargs(self):
        """
        Inject the current request (useful to check the authenticated
        user in the clean* functions for instance).
        """
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs
