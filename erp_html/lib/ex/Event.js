var Event =Class({
// eventElement:null,
 events:{},
 initialize:function()
 {
 // this.eventElement = $("COM_ST_J_Q_EVENT");//����һ��form��
 // if(!this.eventElement.length){
 //  $('body').append(this.eventElement);//����������web��
 // }
 },
 bind:function(event,listener)
 {
  this.events[event]=this.events[event]||[];
  if(this.events[event] instanceof Array)
  {
   this.events[event].push(listener);
  }
 },
 trigger:function(event,target){
  if(this.events[event])
  {
   for(var i in this.events[event])
   {
    this.events[event][i].call(target);
   }
  }
  
 }
});