import { Box, Button, CircularProgress } from '@mui/material';
import Container from '@mui/material/Container';
import { observer } from 'mobx-react';
import { useEffect } from 'react';
import { Loader } from '../components/Loader';
import { PostList } from '../components/PostList';
import { useStore } from '../store/context';

export const HomePage = observer(() => {
    const user = useStore((state) => state.userStore.user);
    const userStore = useStore((state) => state.userStore);
    const postStore = useStore((state) => state.postStore);
    const getPosts = useStore((state) => state.postStore.getPosts);

    useEffect(() => {
        getPosts()
    }, [user]);

    const deletePost = async (id: string) => {
        await postStore.deletePost(Number(id))
        return getPosts()
    }


    const renderPosts = () => {
        if (!user) {
            return null;
        }
        if (postStore.status === "loading") {
            return (
                <Loader />
            )
        }
        return (
            <PostList deletePost={deletePost} posts={postStore.posts} user={user} />
        )
    }

    return (
        <Container maxWidth="md">
            {renderPosts()}
        </Container>
    )
})