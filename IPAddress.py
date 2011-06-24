class IPFormatException(Exception):
       def __init__(self, msg):
                  Exception.__init__(self, msg)

class IPAddress:
  # Construct a new IP Address from the provided bytes
  # Jyothi- Also Am i supposed to join the list to form an ip, when I tried to
  # use join, I see an error no attribute named join, do I have to use a library
  # for this ?
  

  def __init__(self, bytes):
    self.bytes=[]
    length= len(bytes);
    if (length == 0 | length != 4):
      print "Incorrect length: The input list is of length %d,\
      was expecting %d" %(length,4);
      raise IPFormatException("Invalid IP %s" %(bytes))
    else:  
      for i in range(0,length):
        if not 0 < int(bytes[i]) <255:
	  raise IPFormatException(" Invalid value for %dst octet of IP %s, octet range should be between 1-254" %(i+1,bytes))
	else:
	  self.bytes.append(bytes[i]);
    print "The  provided list is %s" %(self.bytes);
    pass
  
  def getByte(self, index):
    return self.bytes[index];

  # determine if this IP Address is equal to another
  # Return false (don't raise an exception) if the other
  # value is not an IP Address
  # Jyothi- How to check that other value is not ip in here? I am doing a check
  # for ip address validity in Init ?Give me a clue, I can work on it.
  def __eq__(self, otherip):
    if((isinstance(otherip,IPAddress)) & (self.bytes== otherip.bytes)):
      return True
    else:
      print "Ip's do not Match";
      return False 

  # Compare this IP Address to another IP Address.  Raise
  # An exception if the other value is not an IP Address
  # Jyothi --- I am not sure on how to raise exception for invalid ip here.
  # The check for invalid ip is in Init... :(
  def __cmp__(self, otherip):
    if((cmp(self.bytes, otherip.bytes))==1):
      print "the output of comparision is %s > %s" %(self.bytes,otherip.bytes);
      return 1
    elif( (cmp(self.bytes, otherip.bytes)) == -1):
      print "the output of comparision is %s < %s" %(self.bytes,otherip.bytes);
      return -1
    else:
      print "IPs are equal";
      return 0

if __name__ == "__main__":
  ip= IPAddress([1,1,1,1]);
  #otherip=IPAddress([abcd]);
  #print(ip.bytes);
  try:
   #print "I am in TRY";
    byte=ip.getByte(0);
   #print byte;
  except :
    print "Index out of range";
  otherip=IPAddress([2,2,2,2]);
  #print "The return value for EQ is %d" %(ip.__eq__(otherip));
  ip.__cmp__(otherip); 


