import sqlite3


class Database:
    
    def __init__(self,db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()


    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?",(user_id,)).fetchall()
            return bool(len(result))


    def add_user(self,user_id,user_name,user_age,user_gender,user_photo,user_content,user_find_gender,user_city,signup):
        with self.connection:
            if self.user_exists(user_id):
                return self.cursor.execute("UPDATE `users` SET `name`=?, `age`=?,`content`=?,`photo`=?,`city`=?, `self_gender`=?,`find_gender`=? WHERE `user_id` = ?", (user_name,user_age,user_content, user_photo, user_city,user_gender,user_find_gender,user_id,))
            else:
                return self.cursor.execute("INSERT INTO `users` (`user_id`,`name`,`age`,`content`,`photo`,`city`,`self_gender`,`find_gender`,`signup`) VALUES (?,?,?,?,?,?,?,?,?)", (user_id,user_name,user_age,user_content, user_photo, user_city,user_gender,user_find_gender,signup,))

    
    def get_user_data(self,user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return result[0]

    
    def get_users_recommend(self,user_id,user_city,user_age,user_find_gender):
        with self.connection:
            #result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id`!=? AND `gender`=? AND `city`=? AND `age` BETWEEN ? AND ?",(user_id,user_gender,user_city,int(user_age)-2,int(user_age)+2)).fetchall()
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id`!=? AND `city`=? AND `self_gender`=? AND `age` BETWEEN ? AND ?",(user_id,user_city,user_find_gender,int(user_age)-2,int(user_age)+5)).fetchall()
            return result


    def update_likes(self,user_id,user_id_like):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `likes`=? WHERE `user_id` = ?", (user_id_like,user_id,))


    def get_likes_data(self,user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `likes` FROM `users` WHERE `user_id`=?",(user_id,)).fetchall()
            return result[0][0]


    def clear_likes(self,user_id):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `likes`=? WHERE `user_id` = ?", (None,user_id,))