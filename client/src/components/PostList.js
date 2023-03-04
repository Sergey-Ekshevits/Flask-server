import { Grid, Typography } from "@mui/material";
import { PostCard } from "./PostCard"

export const PostList = ({ posts }) => {
    console.log(posts.length);
    return (
        <>
            <Typography mt={2} textAlign="center">Посты</Typography>
            <Grid mt={2} container spacing={2} sx={{ alignContent: "stretch" }}>
                {posts?.length && posts.map((post) => {
                    return (
                        <Grid item sm={6} md={6} lg={4} xl={4}>
                            <PostCard post={post} />
                        </Grid>
                    )
                })}
            </Grid>
        </>
    )
}