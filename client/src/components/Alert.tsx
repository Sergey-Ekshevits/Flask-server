import * as React from 'react';
import Box from '@mui/material/Box';
import Alert from '@mui/material/Alert';
import IconButton from '@mui/material/IconButton';
import Collapse from '@mui/material/Collapse';
import Button from '@mui/material/Button';
import CloseIcon from '@mui/icons-material/Close';
import { AlertParamsType, ALERT_EVENT, useAppContext } from '../contexts/AppContext';
import { Container } from '@mui/material';


export default function TransitionAlerts() {
    const [open, setOpen] = React.useState(false);
    const [params, setParams] = React.useState<null | AlertParamsType>(null);
    const appContext = useAppContext()

    const openAlert = (params: AlertParamsType) => {
        setOpen(true)
        setParams(params)
    }
    React.useEffect(() => {
        appContext.eventEmitter.on(ALERT_EVENT, openAlert)
        return () => {
            appContext.eventEmitter.removeListener(ALERT_EVENT, openAlert)
        }
    }, []);

    return (
        <Container maxWidth="md">
            <Box sx={{ width: '100%' }}>
                <Collapse in={open}>
                    <Alert
                        color={params?.type}
                        action={
                            <IconButton
                                aria-label="close"
                                color="inherit"
                                size="small"
                                onClick={() => {
                                    setOpen(false);
                                }}
                            >
                                <CloseIcon fontSize="inherit" />
                            </IconButton>
                        }
                        sx={{ mb: 2, mt: 2 }}
                    >
                        {params?.message}
                    </Alert>
                </Collapse>
            </Box>
        </Container>
    );
}