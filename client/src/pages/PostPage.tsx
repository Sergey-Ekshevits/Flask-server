import { Container, Paper } from "@mui/material"
import { LoginForm } from "../components/LoginForm"
import { Typography } from '@mui/material';
import { useNavigate, useParams } from "react-router-dom";
import { useStore } from "../store/context";
import { Post } from "../components/Post";

export const PostPage = () => {
    const navigate = useNavigate();
    const posts = useStore((state) => state.postStore.posts);
    const { id } = useParams();
    const post = posts.find((p) => {
        return p.id === Number(id)
    })
    return (
        // <Container maxWidth="md">
        //     <Typography mt={2} textAlign="center">PostPage</Typography>
        //     </Container>
        <Paper
            sx={{
                position: 'relative',
                backgroundColor: 'grey.800',
                color: '#fff',
                mb: 4,
                backgroundSize: 'cover',
                backgroundRepeat: 'no-repeat',
                backgroundPosition: 'center',
                // backgroundImage: `url(${post.post_pic})`,
            }}
        >
            <Container maxWidth="md">
                {post && <Post post={post} />}
            </Container>
        </Paper>

    )
}