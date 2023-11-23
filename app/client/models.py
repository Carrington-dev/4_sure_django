from django.db import models

from account.models import User

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'



# class Client(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
#     user = db.relationship("User", back_populates="client") 
#     contact_name = db.Column(db.String(128))
#     contact_email = db.Column(db.String(128))
#     contact_number = db.Column(db.String(16))
