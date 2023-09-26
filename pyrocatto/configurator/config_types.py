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


from collections.abc import Iterable
import logging
from pathlib import Path

import attrs # attrs.asdict
from attrs import define, field, validators
import pyrogram # pyrogram.Client


@define
class PluginConfig:
    root: str = field(validator=validators.instance_of(str))
    include: field(
        validator=validators.optional(
            validator=validators.deep_iterable(
                member_validator=validators.instance_of(str),
                iterable_validator=validators.instance_of(Iterable),
            )
        ))
    exclude: field(
        validator=validators.optional(
            validator=validators.deep_iterable(
                member_validator=validators.instance_of(str),
                iterable_validator=validators.instance_of(Iterable),
            )
        ))

@define
class AddonConfig:
    wheel_userids = field(
        converter=set,
        validator=validators.deep_iterable(
            member_validator=validators.instance_of(int),
            iterable_validator=validators.instance_of(Iterable),
        ),
    )

@define
class ClientConfig:
    name: field(validator=validators.instance_of(str))
    plugin_config: field(validator=validators.instance_of(PluginConfig))
    addon_config: field(validator=validators.instance_of(AddonConfig))

    def create_client(self, session_dir: str) -> pyrogram.Client:
        self.plugin_config = attrs.asdict(self.plugin_config) # pyrogram wants .copy()

        session = Path(
            session_dir,
            self.name + ".session"
        )
        if not session.is_file():
            logging.fatal(f"UNABLE TO LOAD SESSION: {session}")
            logging.fatal("EXITING PYROCATTO-BOT")
            exit(-1)

        client = pyrogram.Client(
            self.name,
            plugins=self.plugin_config,
            workdir=session_dir,
        )
        client.addons = self.addon_config
        return client


__all__ = ["AddonConfig", "PluginConfig", "ClientConfig"]
