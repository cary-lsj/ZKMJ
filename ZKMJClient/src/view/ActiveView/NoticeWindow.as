package view.ActiveView 
{
	import core.Constants;
	import tool.Tool;
	import ui.MahjongRoot.NoticeWindowUI;
	import core.GameIF;
	import core.UiManager;
	import laya.utils.Browser;
	
	/**
	 * ...
	 * @author ...
	 */
	public class NoticeWindow extends NoticeWindowUI 
	{
		
		public function NoticeWindow() 
		{
			super();
		}
		public function Init():void 
		{
			var top:int = (640 - this.height) / 2;
			var left:int = (1136 - this.width) / 2;
			this.pos(left,top);
			Laya.stage.addChild(this);
			var viewNotice:NoticeWindow = this;
			if (Constants.isAdaptPhone)
			{
				reNoticeWindowUi();
			
				Browser.window.addEventListener("resize", function():void {
				Laya.timer.once(1000, viewNotice, reNoticeWindowUi);
				});
			}
		}
			
		private function reNoticeWindowUi():void
		{
			Tool.Adaptation(this);
		}
		public function Destroy():void 
		{
			Laya.stage.removeChild(this);
			this.destroy();
		}
	}

}