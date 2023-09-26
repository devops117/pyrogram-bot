#MIT License
#
#Copyright (c) 2022-2023 DevOps117
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


from collections.abc import Generator
import typing # io.TextIO

from ruamel.yaml import YAML

from ..config_types import ClientConfig, PluginConfig, AddonConfig


def from_yaml(yaml_config: typing.TextIO) -> Generator[ClientConfig]:
    yaml = YAML(typ="safe")
    client_configs = yaml.load(yaml_config)
    client_configs = client_configs["sessions"]

    for name, config in client_configs.items():
        plugin_config = PluginConfig(**config["plugins"])
        addon_config = AddonConfig(**config["addons"])

        yield ClientConfig(
            name,
            plugin_config=plugin_config,
            addon_config=addon_config,
        )


__all__ = ["from_yaml"]
