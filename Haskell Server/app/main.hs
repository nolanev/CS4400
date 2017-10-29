module Main where
import Prelude     (IO)
import Application (appMain)
import Lib 
import Network.Socket
import System.IO
import Control.Exception
import Control.Concurrent
import Control.Monad (when)
import Control.Monad.Fix (fix) 
 
main :: IO ()
main = do
	joinref=0
	--SETUP
	mSocket <- socket AF_INET Stream 0    				-- create socket
    setSocketOption mSocket ReuseAddr 1  				-- make socket immediately reusable - eases debugging. //error on this line
    bind mSocket (SockAddrInet 4242 iNADDR_ANY)   		-- listen on TCP port 4242.
    
	--LISTEN
	listen mSocket 2                              		-- set a max of 2 queued connections
    
	--ACCEPT NEW CONNECTION
	mChannel <- newChan						
	_ <- forkIO $ fix $ \loop -> do
		(_, _) <- readChan mChannel
		loop
	mainLoop mSocket mChannel 0 -- pass my socket and my channel into the mainloop
	
	--To ensure that all of our socket connections are running in the same channel, 
	--we'll have main create it and pass it to mainLoop which will, 
	--pass the channel to each thread in runConn. 

	
	
type Msg = (Int, String) --control current chan controls this messega as a simple fifo buffer with one write adn multiple reads
--"type" also written as "*"

mainLoop :: Socket -> Chan Msg -> Int -> IO ()   -- See how Chan now uses Msg.
mainLoop mSocket mChannel msgNum = do
    conn <- accept mSocket
    forkIO (runConn conn mChannel msgNum)  -- fork for each user. pass the channel to runConn
    mainLoop mSocket mChannel $! msgNum + 1

	
runConn :: (Socket, SockAddr) -> Chan Msg -> Int -> IO ()
runConn (mSocket, _) mChannel msgNum = do						--have run conn duplicate my channel in order to use it
    let broadcast msg = writeChan mChannel (msgNum, msg)
    mHandle <- socketToHandle mSocket ReadWriteMode       		--changes the socket we read in mSocket to a handle 
    hSetBuffering mHandle NoBuffering
 
 
 
	do
 
	 
		hPutStrLn mHandle "Enter chatroom name(JOIN_CHATROOM: [chatroom name]):"					--Writes string to channel managed by handle
		chatname <- fmap init (hGetLine mHandle)
		hPutStrLn mHandle "Enter IP (CLIENT_IP: [IP Address of client if UDP | 0 if TCP]):"				
		clientip <- fmap init (hGetLine mHandle)
		hPutStrLn mHandle "Enter port num (PORT: [port number of client if UDP | 0 if TCP]):"				
		clientport <- fmap init (hGetLine mHandle)
		hPutStrLn mHandle "Enter name (CLIENT_NAME: [string Handle to identifier client user]):"				
		clientname <- fmap init (hGetLine mHandle)
		--JOIN_CHATROOM: [chatroom name]
		  --CLIENT_IP: [IP Address of client if UDP | 0 if TCP]
		  --PORT: [port number of client if UDP | 0 if TCP]
		  --CLIENT_NAME: [string Handle to identifier client user]
		roomref=1
		joinref= joinref++
				
		broadcast ("--> " ++ clientname ++ " entered chat.")
		hPutStrLn mHandle ("JOINED_CHATROOM: " + clientname + "\n SERVER_IP: " + clientip + "\n PORT: " + clientport + "\n ROOM_REF: " + roomRef + "\n JOIN_ID: " + joinID)
		 -- SERVER_IP: [IP address of chat room]
		  --PORT: [port number of chat room]
		  --ROOM_REF: [integer that uniquely identifies chat room on server]
		  --JOIN_ID: [integer that uniquely identifies client joining]")
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
             _      -> broadcast (clientname ++ ": " ++ line) >> loop
 
    killThread reader                      -- kill after the loop ends
    broadcast ("<-- " ++ clientname ++ " left.") -- make a final broadcast
    hClose mHandle                             -- close the handle
   
   
   