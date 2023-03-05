import * as React from 'react';
import { styled } from '@mui/material/styles';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import CardActions from '@mui/material/CardActions';
import Collapse from '@mui/material/Collapse';
import Avatar from '@mui/material/Avatar';
import IconButton, { IconButtonProps } from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import { red } from '@mui/material/colors';
import FavoriteIcon from '@mui/icons-material/Favorite';
import ShareIcon from '@mui/icons-material/Share';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import MoreVertIcon from '@mui/icons-material/MoreVert';
import { STATIC_POST_URL } from '../constant';
import * as DOMPurify from 'dompurify';
import { Menu, MenuItem } from '@mui/material';
import { Link, NavLink } from "react-router-dom";
import { PostDto } from "../types";
import { EmptyPicture } from './EmptyPicture';

interface ExpandMoreProps extends IconButtonProps {
    expand: boolean;
}

const ExpandMore = styled((props: ExpandMoreProps) => {
    const { expand, ...other } = props;
    return <IconButton {...other} />;
})(({ theme, expand }) => ({
    transform: !expand ? 'rotate(0deg)' : 'rotate(180deg)',
    marginLeft: 'auto',
    transition: theme.transitions.create('transform', {
        duration: theme.transitions.duration.shortest,
    }),
}));


type Props = {
    post: PostDto;
    isOwner: boolean;
}
const menu = [{ title: "Удалить", action: "delete" }, { title: "Редактировать", action: "edit" }]

export const PostCard = ({ post, isOwner }: Props) => {
    const [expanded, setExpanded] = React.useState(false);
    const [anchorElNav, setAnchorElNav] = React.useState(null);

    const handleExpandClick = () => {
        setExpanded(!expanded);
    };

    const handleOpenUserMenu = (event: any) => {
        setAnchorElNav(event.currentTarget);
    };

    const handleClosUserMenu = (action: string) => {
        console.log(action);
        setAnchorElNav(null);
    };



    const data = new Date(Number(post.date_created))

    const renderTitle = () => {
        return (
            <Typography style={{
                overflow: "hidden",
                textOverflow: "ellipsis",
                whiteSpace: "nowrap",
                maxWidth: "140px"
            }}>
                {post.title}
            </Typography>

        )
    }

    const renderMenu = () => {
        return (
            <Menu
                id="menu-appbar"
                anchorEl={anchorElNav}
                anchorOrigin={{
                    vertical: 'bottom',
                    horizontal: 'right',
                }}
                keepMounted
                transformOrigin={{
                    vertical: 'top',
                    horizontal: 'right',
                }}
                open={Boolean(anchorElNav)}
                onClose={() => handleClosUserMenu("close")}

            >
                {menu.map((item) => (
                    <MenuItem key={item.action} onClick={() => handleClosUserMenu(item.action)}>
                        <Typography textAlign="center">{item.title}</Typography>
                    </MenuItem>
                ))}
            </Menu>
        )
    }

    const renderPicture = () => {
        if (!post.post_pic) {
            return (
                <EmptyPicture height={"194"} />
            )
        }
        return (
            <CardMedia
                component="img"
                height="194"
                image={STATIC_POST_URL + "/" + post.post_pic}
                alt="Paella dish"
            />
        )
    }
    return (
        <Card sx={{ maxWidth: 345, height: "100%", display: "flex", flexDirection: "column" }}>
            <CardHeader
                disableTypography={false}
                avatar={
                    <Avatar sx={{ bgcolor: red[500] }} aria-label="recipe">
                        R
                    </Avatar>
                }
                action={
                    <>
                        {isOwner && (<>
                            <IconButton onClick={handleOpenUserMenu} aria-label="settings">
                                <MoreVertIcon />
                            </IconButton>
                            {renderMenu()}
                        </>)
                        }
                    </>
                }
                title={renderTitle()}
                subheader={data.toDateString()}
            />
            <Link to={`/post/${post.id}`} style={{ textDecoration: "none" }}>

                {renderPicture()}

                <CardContent>
                    <Typography component={'span'} variant="body2" color="text.secondary">
                        <div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(post.body) }} />
                    </Typography>
                </CardContent>
            </Link>
            {/* <CardActions disableSpacing sx={{ marginTop: "auto" }}>
                <IconButton aria-label="add to favorites">
                    <FavoriteIcon />
                </IconButton>
                <IconButton aria-label="share">
                    <ShareIcon />
                </IconButton>
                <ExpandMore
                    expand={expanded}
                    onClick={handleExpandClick}
                    aria-expanded={expanded}
                    aria-label="show more"
                >
                    <ExpandMoreIcon />
                </ExpandMore>
            </CardActions>
            <Collapse in={expanded} timeout="auto" unmountOnExit>
                <CardContent>
                    <Typography paragraph>Method:</Typography>
                    <Typography paragraph>
                        Heat 1/2 cup of the broth in a pot until simmering, add saffron and set
                        aside for 10 minutes.
                    </Typography>
                    <Typography paragraph>
                        Heat oil in a (14- to 16-inch) paella pan or a large, deep skillet over
                        medium-high heat. Add chicken, shrimp and chorizo, and cook, stirring
                        occasionally until lightly browned, 6 to 8 minutes. Transfer shrimp to a
                        large plate and set aside, leaving chicken and chorizo in the pan. Add
                        pimentón, bay leaves, garlic, tomatoes, onion, salt and pepper, and cook,
                        stirring often until thickened and fragrant, about 10 minutes. Add
                        saffron broth and remaining 4 1/2 cups chicken broth; bring to a boil.
                    </Typography>
                    <Typography paragraph>
                        Add rice and stir very gently to distribute. Top with artichokes and
                        peppers, and cook without stirring, until most of the liquid is absorbed,
                        15 to 18 minutes. Reduce heat to medium-low, add reserved shrimp and
                        mussels, tucking them down into the rice, and cook again without
                        stirring, until mussels have opened and rice is just tender, 5 to 7
                        minutes more. (Discard any mussels that don&apos;t open.)
                    </Typography>
                    <Typography>
                        Set aside off of the heat to let rest for 10 minutes, and then serve.
                    </Typography>
                </CardContent>
            </Collapse> */}
        </Card>
    );
}