from telegram.classes.Message import Message
from telegram.classes.InlineQuery import InlineQuery
from telegram.classes.ChosenInlineResult import ChosenInlineResult
from telegram.classes.CallbackQuery import CallbackQuery
from telegram.classes.ShippingQuery import ShippingQuery
from telegram.classes.PreCheckoutQuery import PreCheckoutQuery
from telegram.classes.Poll import Poll
from telegram.classes.PollAnswer import PollAnswer
from telegram.classes.ChatMemberUpdated import ChatMemberUpdated
from telegram.classes.ChatJoinRequest import ChatJoinRequest

class Update:
    update_id : int
    Message : Message
    edited_message : Message
    channel_post : Message
    edited_channel_post : Message
    inline_query : InlineQuery
    chosen_inline_result : ChosenInlineResult
    callback_query : CallbackQuery
    shipping_query : ShippingQuery
    pre_checkout_query : PreCheckoutQuery
    poll : Poll
    poll_answer : PollAnswer
    my_chat_member : ChatMemberUpdated
    chat_member : ChatMemberUpdated
    chat_join_request : ChatJoinRequest
    def __init__(self,**kwargs):
        self.update_id = kwargs.get('update_id')
        self.Message = Message(**kwargs.get('message')) if kwargs.get('message') else None
        self.edited_message = Message(**kwargs.get('edited_message')) if kwargs.get('edited_message') else None
        self.channel_post = Message(**kwargs.get('channel_post')) if kwargs.get('channel_post') else None
        self.edited_channel_post = Message(**kwargs.get('edited_channel_post')) if kwargs.get('edited_channel_post') else None
        self.inline_query = InlineQuery(**kwargs.get('inline_query')) if kwargs.get('inline_query') else None
        self.chosen_inline_result = ChosenInlineResult(**kwargs.get('chosen_inline_result')) if kwargs.get('chosen_inline_result') else None
        self.callback_query = CallbackQuery(**kwargs.get('callback_query')) if kwargs.get('callback_query') else None
        self.shipping_query = ShippingQuery(**kwargs.get('shipping_query')) if kwargs.get('shipping_query') else None
        self.pre_checkout_query = PreCheckoutQuery(**kwargs.get('pre_checkout_query')) if kwargs.get('pre_checkout_query') else None
        self.poll = Poll(**kwargs.get('poll')) if kwargs.get('poll') else None
        self.poll_answer = PollAnswer(**kwargs.get('poll_answer')) if kwargs.get('poll_answer') else None
        self.my_chat_member = ChatMemberUpdated(**kwargs.get('my_chat_member')) if kwargs.get('my_chat_member') else None
        self.chat_member = ChatMemberUpdated(**kwargs.get('chat_member')) if kwargs.get('chat_member') else None
        self.chat_join_request = ChatJoinRequest(**kwargs.get('chat_join_request')) if kwargs.get('chat_join_request') else None
