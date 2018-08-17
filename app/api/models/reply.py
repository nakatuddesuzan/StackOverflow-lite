replies_list = []

class Reply:
    def __init__(self, user_id, qtn_id, reply_desc):
        self.reply_desc = reply_desc
        self.qtn_id = qtn_id
        self.user_id = user_id