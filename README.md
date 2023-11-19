# Takt Plugin Template

Use this template as a starting point to create new takt plugins. Choose a
descriptive name and replace the `plugin` placeholder in `takt_plugin.py` and
`pyproject.toml` references.


For example:

- Rename `takt_plugin.py` to `takt_metrics.py`.
- Update `pyproject.toml` accordingly, for example, change the value of `name`
  to `"takt_metrics"`.

> [!WARNING]
>
> Takt uses the prefix `takt_` to locate plugins.


## Test

Here is a simple example of how you can test your plugin.

```bash
python -m venv venv
source venv/bin/activate
pip install git+https://github.com/mmngreco/takt
pip install .
takt --help
takt <your-plugin>
```


> [!WARNING]
>
> To make the plugin work, you need to install it in non-editable mode.
> Otherwise, `takt` will not be able to detect the plugin.
