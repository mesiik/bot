import logging, sys, pathlib, sys

PATH = pathlib.Path(__file__).parent


LOGPATH = PATH.parent.joinpath("file.log")

def setup_logging() -> None:
    log = logging.getLogger()
    logging.getLogger("discord").setLevel(logging.WARNING)
    logging.getLogger("pyppeteer").setLevel(logging.INFO)
    logging.getLogger('aiohttp').setLevel(logging.WARNING)


    log.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler(sys.stdout)
    file_handler = logging.FileHandler(filename=LOGPATH, mode="w", encoding="utf-8")
    console_handler.setLevel(logging.INFO)
    file_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s:%(module)s:%(process)d] %(message)s"))
    file_handler.setFormatter(logging.Formatter("[%(levelname)s] %(asctime)s %(name)s[%(process)d] %(message)s"))
    log.addHandler(console_handler)
    log.addHandler(file_handler)