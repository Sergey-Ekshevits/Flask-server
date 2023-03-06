
export type PostDto = {
    title: string;
    body: string;
    id: string;
    post_pic: string;
    date_created: string;
    user: UserDto;
}

export type UserDto = {
    name: string,
    email: string,
    avatar_url: string;
}
export type LocalStorageDto = {
    access_token: string, refresh_token: string, user: UserDto
}

export const TExt = ""