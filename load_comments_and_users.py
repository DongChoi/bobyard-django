import json
from datetime import datetime
from comments.models import Comment, User



def create_or_get_user(username):
    # Check if the user already exists
    user, created = User.objects.get_or_create(user_name=username)
    return user

# Check if there are no existing records in the Comment model
if not Comment.objects.exists():
    with open('comments/comments.json') as f:
        comments_data = json.load(f)

    for comment_data in comments_data['comments']:
        comment_data['date'] = datetime.strptime(comment_data['date'], '%Y-%m-%dT%H:%M:%SZ')

        # Get or create the user
        user = create_or_get_user(comment_data['author'])
        # Create the comment with the associated user
        Comment.objects.create(author=user, text=comment_data['text'], date=comment_data['date'], likes=comment_data['likes'], image=comment_data['image'])

    print("Data loaded successfully.")
else:
    print("Data already exists in the database.")