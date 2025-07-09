from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class ChatSession(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title


class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name="messages")
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
