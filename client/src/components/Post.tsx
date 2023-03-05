import { Box, Grid, Link, Paper, Typography } from "@mui/material"
import DOMPurify from "dompurify";
import { PostDto } from "../types";

type Props = {
    post: PostDto
}
export const Post = ({ post }: Props) => {
    return (
        <>
            {/* Increase the priority of the hero background image */}
            {<img style={{ display: 'none' }} src={post.post_pic} alt={post.title} />}
            <Box
                sx={{
                    position: 'absolute',
                    top: 0,
                    bottom: 0,
                    right: 0,
                    left: 0,
                    backgroundColor: 'rgba(0,0,0,.3)',
                }}
            />
            <Grid container>
                <Grid item md={12}>
                    <Box
                        paddingTop={6}
                        paddingBottom={6}
                        sx={{
                            position: 'relative',
                            pr: { md: 0 },
                        }}
                    >
                        <Typography component="h1" variant="h3" color="inherit" gutterBottom>
                            {post.title}
                        </Typography>
                        <Typography component={'span'} variant="body2" color="inherit" >
                            <div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(post.body) }} />
                        </Typography>
                        {/* <Link variant="subtitle1" href="#">
                            {post.linkText}
                        </Link> */}
                    </Box>
                </Grid>
            </Grid>
        </>
    )
}