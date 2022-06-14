from discord.ext import commands


class SubcommandInvocationRequired(commands.CommandError):
    pass

class Command(commands.Command):
    def __init__(self, *args, typing: bool = False, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.typing = typing

    async def invoke(self, ctx):
        if self.typing:
            async with ctx.typing():
                await super().invoke(ctx)
        else:
            await super().invoke(ctx)

class Group(commands.Group, Command):
    def __init__(self, *args, hollow: bool = False, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.hollow = hollow

    async def invoke(self, ctx):
        if ctx.view.eof and self.hollow:
            raise SubcommandInvocationRequired()
        await super().invoke(ctx)

    def Feature(self, *args, **kwargs):
        def decorator(func):
            kwargs.setdefault("parent", self)
            result = Feature(*args, **kwargs)(func)
            self.add_command(result)
            return result

        return decorator

    def group(self, *args, **kwargs):
        def decorator(func):
            kwargs.setdefault("parent", self)
            result = group(*args, **kwargs)(func)
            self.add_command(result)
            return result

        return decorator


def Feature(name: str = None, cls=Command, **kwargs):
    return commands.command(name, cls, **kwargs)

def group(name: str = None, **kwargs):
    return Feature(name, Group, **kwargs)