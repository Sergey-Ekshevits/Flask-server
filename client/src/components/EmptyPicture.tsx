

type Props = {
    height: string;
}
export const EmptyPicture = ({ height }: Props) => {
    
    return (
        <div style={{
            height: `${height}px`,
            width: "100%",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            backgroundColor: "GrayText"
        }}>
            <svg xmlns="http://www.w3.org/2000/svg" fill="#000000" width="50px" height="50px" viewBox="0 0 24 24">
                <path d="M21,2H3A1,1,0,0,0,2,3V21a1,1,0,0,0,1,1H21a1,1,0,0,0,1-1V3A1,1,0,0,0,21,2ZM20,14l-3-3-5,5-2-2L4,20V4H20ZM6,8.5A2.5,2.5,0,1,1,8.5,11,2.5,2.5,0,0,1,6,8.5Z" />
            </svg>
        </div>
    );
}
