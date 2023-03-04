import { useEffect } from 'react';
import { useStore } from '../store/context';

export const PostList = () => {
    const posts = useStore((state) => state.postStore.posts);
    const getPosts = useStore((state) => state.postStore.getPosts);
    useEffect(() => {
        getPosts()
    },[])
    return (
        <ul>
            {posts && posts.map((post) => {
                return (
                    <li>
                        <h3>{post.title}</h3>
                        <div dangerouslySetInnerHTML={{ __html: post.body }} />
                    </li>
                )
            })}
        </ul>
    )
}