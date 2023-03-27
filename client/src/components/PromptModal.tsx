import * as React from 'react';
import { BasicModal } from './BasicModal';
import { Button, Stack, Typography } from '@mui/material';



type Props = {
    isOpen?: boolean;
    children?: React.ReactNode;
    onClose: () => void;
    onClick: (value: boolean) => void;
}


export function PromptModal({ isOpen, onClose, onClick }: Props) {

    return (
        <BasicModal
            isOpen={isOpen}
            onClose={onClose}
        >
            <Typography id="modal-modal-title" variant="h6" component="h2">
                Вы уверены что хотите удалить?
            </Typography>
            <Stack spacing={2} direction="row">
                <Button variant="contained" onClick={() => onClick(true)}>Да</Button>
                <Button variant="outlined" onClick={() => onClick(false)}>Нет</Button>
            </Stack>
        </BasicModal>
    );
}