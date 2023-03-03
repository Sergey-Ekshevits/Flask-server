import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';
import { PostList } from "./components/PostList"
import { RegistrateForm } from "./components/RegistrateForm"
import { LoginForm } from "./components/LoginForm"
import { restService } from "./services/RestService"
import { observer } from "mobx-react"

const App = observer(() => {
  const [posts, setPosts] = useState([])
  useEffect(() => {
    console.log(restService.getHeader());
    const getPosts = async () => {
      const posts = await restService.post("http://192.168.1.34:5000/api/posts").then((res) => res.json()).catch(() => [])
      console.log(posts);
      setPosts(posts)
    }
    getPosts()
  }, [])
  return (
    <div className="App">
      <header className="App-header">
        {/* <PostList posts={posts} /> */}
        <RegistrateForm />
        <LoginForm />
      </header>
    </div>
  );
})

export default App;
