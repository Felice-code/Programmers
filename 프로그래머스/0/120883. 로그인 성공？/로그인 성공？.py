def solution(id_pw, db):
    id, pw = id_pw
    for user_id, user_pw in db:
        if user_id == id:
            return "login" if user_pw == pw else "wrong pw"
    return "fail"
