from bot.helper.ext_utils.bot_utils import COMMAND_USAGE, new_task
from bot.helper.ext_utils.help_messages import (
    CLONE_HELP_DICT,
    MIRROR_HELP_DICT,
    YT_HELP_DICT,
    help_string,
)
from bot.helper.telegram_helper.button_build import ButtonMaker
from bot.helper.telegram_helper.message_utils import (
    delete_message,
    edit_message,
    send_message,
)


@new_task
async def arg_usage(_, query):
    data = query.data.split()
    message = query.message
    if data[1] == "close":
        await delete_message(message)
    elif data[1] == "back":
        if data[2] == "m":
            await edit_message(
                message,
                COMMAND_USAGE["mirror"][0],
                COMMAND_USAGE["mirror"][1],
            )
        elif data[2] == "y":
            await edit_message(
                message,
                COMMAND_USAGE["yt"][0],
                COMMAND_USAGE["yt"][1],
            )
        elif data[2] == "c":
            await edit_message(
                message,
                COMMAND_USAGE["clone"][0],
                COMMAND_USAGE["clone"][1],
            )
    elif data[1] == "mirror":
        buttons = ButtonMaker()
        buttons.data_button("Back", "help back m")
        button = buttons.build_menu()
        await edit_message(message, MIRROR_HELP_DICT[data[2]], button)
    elif data[1] == "yt":
        buttons = ButtonMaker()
        buttons.data_button("Back", "help back y")
        button = buttons.build_menu()
        await edit_message(message, YT_HELP_DICT[data[2]], button)
    elif data[1] == "clone":
        buttons = ButtonMaker()
        buttons.data_button("Back", "help back c")
        button = buttons.build_menu()
        await edit_message(message, CLONE_HELP_DICT[data[2]], button)


@new_task
async def bot_help(_, message):
    await send_message(message, help_string)
