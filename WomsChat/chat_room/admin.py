from django.contrib import admin
from chat_room.models import * 




class RoomAdmin(admin.ModelAdmin):
   list_display = ("creater","invited_user","date")

   def invited_user(self, obj):
     return "\n".join([user.username for user in obj.invited.all()])

admin.site.register(Room,RoomAdmin)



class ChatAdmin(admin.ModelAdmin):
   list_display = [field.name for field in Chat._meta.fields]
admin.site.register(Chat,ChatAdmin)

