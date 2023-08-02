class Poll:
    id : str
    question : str
    options : list[PollOption]
    total_voter_count : int
    is_closed : bool
    is_anonymous : bool
    type : str
    allows_multiple_answers : bool
    correct_option_id : int
    explanation : str
    explanation_entities : list[MessageEntity]
    open_period : int
    close_date : int
    def __init__(self,**kwargs):
        self.id = kwargs.get('id')
        self.question = kwargs.get('question')
        self.options = [PollOption(**x) for x in kwargs.get('options')]
        self.total_voter_count = kwargs.get('total_voter_count')
        self.is_closed = kwargs.get('is_closed')
        self.is_anonymous = kwargs.get('is_anonymous')
        self.type = kwargs.get('type')
        self.allows_multiple_answers = kwargs.get('allows_multiple_answers')
        self.correct_option_id = kwargs.get('correct_option_id')
        self.explanation = kwargs.get('explanation')
        self.explanation_entities = [MessageEntity(**x) for x in kwargs.get('explanation_entities')]
        self.open_period = kwargs.get('open_period')
        self.close_date = kwargs.get('close_date')