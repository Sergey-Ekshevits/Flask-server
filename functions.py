from werkzeug.utils import secure_filename
import os
from os.path import join, dirname, realpath, splitext
import uuid
UPLOADS_PATH = join(dirname(realpath(__file__)), '.\\static\\')
UPLOADS_AVATAR_PATH = join(dirname(realpath(__file__)), '.\\static\\avatars')
UPLOADS_POST_PIC_PATH = join(dirname(realpath(__file__)), '.\\static\\post-picture')

def upload_pic(file,folder,post):
    if not os.path.exists(UPLOADS_PATH+folder):
        os.mkdir(UPLOADS_PATH+folder)
    # if new:
        # if post.post_pic:
        #     delete_file(post.post_pic)
    file_ext = splitext(secure_filename(file.filename))[1]
    filename = str(uuid.uuid4()) + file_ext
    path = join(UPLOADS_PATH+folder, filename)
    file.save(path)
    # print(path)
    # print(file)
    return filename

def upload_avatar(file, user):
    if not os.path.exists(UPLOADS_AVATAR_PATH):
        os.mkdir(UPLOADS_AVATAR_PATH)
    if user.avatar_url:
        delete_file(user.avatar_url)
    file_ext = splitext(secure_filename(file.filename))[1]
    filename = str(uuid.uuid4()) + file_ext
    path = join(UPLOADS_AVATAR_PATH, filename)
    file.save(path)
    return filename
    # return redirect(url_for('uploaded_file',
    #                         filename=filename))
def delete_file(filename, folder=''):
    path = join(UPLOADS_PATH+folder, filename)
    if os.path.isfile(path):
        os.remove(path)

