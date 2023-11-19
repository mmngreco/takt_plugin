"""
The plugin_name required for the Takt.register decorator is the name of the
section in the help menu.

NOTE: Avoid instantiating the Takt class in the global scope of the plugin,
this will cause circular imports and break the plugin system.
"""
from takt import Takt

PLUGIN_NAME = __name__


@Takt.register(name="cmd_renamed", plugin_name=PLUGIN_NAME)
def my_command():
    # Use Takt as interface to the Takt application
    t = Takt()
    t.print_console(f"Hello from my plugin: {t}!")


@Takt.register(plugin_name=PLUGIN_NAME)
def my_command2():
    # Use Takt as interface to the Takt application
    t = Takt()
    t.print_console(f"Hello from my plugin: {t}!")
