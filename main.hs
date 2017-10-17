--Haskell mSocket programme pt 1
-- in Main.hs
module Main where
 
import Network.Socket
import System.IO
import Control.Concurrent			--threads and concurrent control libraray
import Control.Monad (when)
import Control.Monad.Fix (fix)
import Control.Exception
 
main :: IO ()
main = do
	--SETUP
	mSocket <- socket AF_INET Stream 0    				-- create socket
    setSocketOption mSocket ReuseAddr 1  				-- make socket immediately reusable - eases debugging.
    bind mSocket (SockAddrInet 4242 iNADDR_ANY)   		-- listen on TCP port 4242.
    
	--LISTEN
	listen mSocket 2                              		-- set a max of 2 queued connections
    
	--ACCEPT NEW CONNECTION
	mChannel <- newChan
	_ <- forkIO $ fix $ \loop -> do
		(_, _) <- readChan mChannel
		loop
	mainLoop mSocket mChannel 0 -- pass my socket and my channel into the loop
	
type Msg = (Int, String)

mainLoop :: Socket -> Chan Msg -> Int -> IO ()   -- See how Chan now uses Msg.
mainLoop mSocket mChannel msgNum = do
    conn <- accept mSocket
    forkIO (runConn conn mChannel)  -- fork for each user. pass the channel to runConn
    mainLoop mSocket mChannel $! msgNum + 1

runConn :: (Socket, SockAddr) -> Chan Msg -> Int -> IO ()
runConn (mSocket, _) mChannel msgNum = do
    let broadcast msg = writeChan mChannel (msgNum, msg)
    mHandle <- socketToHandle mSocket ReadWriteMode       			--changes the socket we read in mSocket to a handle 
    hSetBuffering mHandle NoBuffering
 
    hPutStrLn mHandle "Hi, what's your name?"					--Writesstring to channel managed by handle
    name <- fmap init (hGetLine mHandle)
    broadcast ("--> " ++ name ++ " entered chat.")
    hPutStrLn mHandle ("Welcome, " ++ name ++ "!")
    commLine <- dupChan mChannel
	
	-- fork off a thread for reading from the duplicated channel
    reader <- forkIO $ fix $ \loop -> do
        (nextNum, line) <- readChan commLine
        when (msgNum /= nextNum) $ hPutStrLn mHandle line
        loop
 
    handle (\(SomeException _) -> return ()) $ fix $ \loop -> do
        line <- fmap init (hGetLine mHandle)
        case line of
             -- If an exception is caught, send a message and break the loop
             "quit" -> hPutStrLn mHandle "Bye!"
             -- else, continue looping.
             _      -> broadcast (name ++ ": " ++ line) >> loop
 
    killThread reader                      -- kill after the loop ends
    broadcast ("<-- " ++ name ++ " left.") -- make a final broadcast
    hClose mHandle                             -- close the handle
   
   
   
   
   --https://www.haskell.org/cabal/users-guide/developing-packages.html