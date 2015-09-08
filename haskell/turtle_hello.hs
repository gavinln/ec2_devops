
{-# LANGUAGE OverloadedStrings #-}

import Turtle

datePwd :: IO UTCTime -- type signature
datePwd = do
  dir <- pwd
  datefile dir

shellCmd :: IO ExitCode
shellCmd = do
  result <- shell "dir" empty
  return result


checkedShellCmd :: IO ()
checkedShellCmd = do
  result <- shell "dire" empty
  case result of
    ExitSuccess   -> return ()
    ExitFailure n -> die ("failed with exit code: " <> repr n)

-- main :: IO ()         -- type signature
main2 :: IO ExitCode
main2 = do
  echo "Hello, World!"
  echo "Line 2"
  dir <- pwd
  print dir
  time <- datePwd
  print time
  echo $ format (" The time of the working dir is " %s) $ repr time
  -- checkedShellCmd
  result <- shellCmd
  return ExitSuccess

main :: IO ExitCode
main = do
  view pwd
  currentDir <- pwd
  view ( find "hello.hs" ".")
  return ExitSuccess
