from django.db import models

# Create your models here.


class User(models.Model):
    def __str__(self):
        return f"id: {self.id}, user_name: {self.user_name}, is_admin: {self.is_admin}"
    user_name = models.CharField(max_length=200)
    is_admin = models.BooleanField(default=False)

class Comment(models.Model):
    def __str__(self):
        return f"id: {self.id}, user: {self.author.user_name}, parent_comment: {self.parent_comment}, comment_text: {self.text}"
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)  # Set default value to 0
    image = models.URLField(null=True, blank=True)

    def serialize(self):
        serialized_comment = {"author": self.author.pk, "parent_comment": self.parent_comment,
                              "text": self.text, "date" : self.date, "likes": self.likes,
                              "image": self.image, "id": self.pk}
        return serialized_comment
