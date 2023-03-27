import { Box, Button, CircularProgress } from '@mui/material';
import Container from '@mui/material/Container';
import { observer } from 'mobx-react';
import { useEffect, useRef, useState } from 'react';
import { Loader } from '../components/Loader';
import { PostList } from '../components/PostList';
import { PromptModal } from '../components/PromptModal';
import { useStore } from '../store/context';

export const HomePage = observer(() => {
    const user = useStore((state) => state.userStore.user);
    const confirmationCallbackRef = useRef<((value: boolean) => void) | null>(null);
    const [openPrompt, setOpenPrompt] = useState(false);
    const userStore = useStore((state) => state.userStore);
    const postStore = useStore((state) => state.postStore);
    const getPosts = useStore((state) => state.postStore.getPosts);

    useEffect(() => {
        getPosts()
    }, [user]);

    const handleDeletePost = async (id: string) => {
        setOpenPrompt(true);
        try {
          const response = await new Promise((resolve) => {
            confirmationCallbackRef.current = resolve; // сохраняем callback в реф
          });
          if (response) {
            await postStore.deletePost(Number(id));
            await getPosts();
          }
        } finally {
          confirmationCallbackRef.current = null; // очищаем callback из рефа
          setOpenPrompt(false);
        }
      };
    
      const handleModalResponse = (response: boolean) => {
        if (confirmationCallbackRef.current) {
          confirmationCallbackRef.current(response); // вызываем сохраненный callback из рефа
        }
      };

      const closeModal = () => {
        if (confirmationCallbackRef.current) {
          confirmationCallbackRef.current(false); // вызываем сохраненный callback из рефа
        }
        setOpenPrompt(false);
      };
    


    const renderPosts = () => {
        if (!user) {
            return null;
        }
        // if (postStore.status === "loading") {
        //     return (
        //         <Loader />
        //     )
        // }
        return (
            <PostList deletePost={handleDeletePost} posts={postStore.posts} user={user} />
        )
    }

    return (
        <Container maxWidth="md">
            <PromptModal isOpen={openPrompt} onClose={closeModal} onClick={handleModalResponse} />
            {renderPosts()}
        </Container>
    )
})