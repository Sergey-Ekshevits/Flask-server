import { Box, CircularProgress } from "@mui/material";

interface LoaderProps {

}

export const Loader = ({}: LoaderProps)  => {
    return (
        <Box mt={9} sx={{ display: "flex", alignItems: "center", justifyContent: "center" }}>
            <CircularProgress />
        </Box>
    );
}
