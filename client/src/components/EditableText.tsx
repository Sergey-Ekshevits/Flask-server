import { Box, Button, IconButton, TextField, Typography } from "@mui/material";
import { useEffect, useRef, useState } from "react";
import Edit from '@mui/icons-material/Edit';
import { useFormControl } from '@mui/material/FormControl';
interface EditableTextProps {
    value: string | null;
    title?: string;
    onEdit: (value: string) => void;
}

const EditableText = ({ value, title, onEdit }: EditableTextProps) => {
    const [edit, setEdit] = useState(false)
    const inputRef = useRef<HTMLDivElement | null>(null)

    useEffect(() => {
        console.log({ edit });

        if (edit) {
            console.log({ inputRef });

            inputRef?.current?.focus()
        }
    }, [edit])
    const renderTextComponent = () => {
        if (edit) {
            return (
                <TextField
                    inputRef={inputRef}
                    focused
                    onChange={(e: any) => onEdit(e.target.value)}
                    defaultValue={value} id="standard-basic"
                    variant="standard" />
            )
        }

        return (
            <>
                <Typography variant="subtitle1" color="text.secondary" sx={{ minHeight: "32px" }}>
                    {value}
                </Typography>
            </>
        )
    }

    return (
        <Box sx={{
            display: "flex",
            justifyContent: "space-between"
        }}>
            <Box>
                <Typography component="p" variant="h6">
                    {title}
                </Typography>
                {renderTextComponent()}
            </Box>

            <IconButton
                size="large"
                aria-label="account of current user"
                aria-controls="menu-appbar"
                aria-haspopup="true"
                onClick={() => setEdit((prev) => !prev)}
                color="primary"
            >
                <Edit />
            </IconButton>
        </Box>
    );
}

export default EditableText;