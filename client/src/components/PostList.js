


export const PostList = ({ posts }) => {
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