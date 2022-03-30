class BootstrapFormMixin:
    fields = {}

    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += 'form-control'
