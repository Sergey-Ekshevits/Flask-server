import Container from '@mui/material/Container';
import { observer } from 'mobx-react';
import { useEffect } from 'react';
import { PostList } from '../components/PostList';
import { useStore } from '../store/context';

export const HomePage = observer(() => {
    const user = useStore((state) => state.userStore.user);
    const posts = useStore((state) => state.postStore.posts);
    const getPosts = useStore((state) => state.postStore.getPosts);

    useEffect(() => {
        if (user) {
            getPosts()
        }
    }, []);
    useEffect(() => {
        if (user) {
            getPosts()
        }
    }, [user]);

    return (
        <Container maxWidth="md">
            {user && <PostList posts={posts} />}
            <div style={{ padding: 20 }}>
                <h2>Home View</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adip.</p>
            </div>
        </Container>
    )
})