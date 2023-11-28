css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://static.wixstatic.com/media/6f8f29_3e2c20a5ae86460e814fd3a3eac98f42~mv2.png/v1/crop/x_50,y_67,w_850,h_852/fill/w_160,h_160,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Group%20127.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://www.iconpacks.net/icons/2/free-user-icon-3297-thumb.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
