import { Grid, Typography } from "@mui/material";
import { PostCard } from "./PostCard"

export const PostList = ({ posts, user, deletePost }) => {
    
    return (
        <>
            <Typography mt={2} textAlign="center">Посты</Typography>
            {!posts?.length && (
                <Typography mt={6} textAlign="center">Нет постов</Typography>
            )}
            <Grid mt={2} container spacing={2} sx={{ alignContent: "stretch" }}>

                {posts?.length && posts.map((post) => {
                    return (
                        <Grid key={post.id} item sm={6} md={6} lg={4} xl={4}>
                            <PostCard deletePost={deletePost} post={post} isOwner={user?.id === post.user.id} />
                        </Grid>
                    )
                })}
            </Grid>
        </>
    )
}