import EventEmitter from 'events';
import { createContext, useContext } from 'react';

export const ALERT_EVENT = "ALERT_EVENT"

export type AppContextType = {
  eventEmitter: EventEmitter;
}

export type AppProvideProps = {
  value: AppContextType;
  children: React.ReactNode;
}

export type AlertParamsType = {
  message: string;
  type: "success" | "error" | "warning";
}

export const AppContext = createContext<null | AppContextType>(null);
export function useAppContext(): AppContextType
export function useAppContext() {
  const appContext = useContext(AppContext);
  return appContext;
}

export function useEventAlert() {
  const eventEmitter = useAppContext();
  return (params: AlertParamsType) => eventEmitter.eventEmitter.emit(ALERT_EVENT, params);
}

export function AppProvider(props: AppProvideProps) {
  return (
    <AppContext.Provider value={props.value}>
      {props.children}
    </AppContext.Provider>
  );
}