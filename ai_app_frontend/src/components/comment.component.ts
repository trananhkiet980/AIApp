



import { Component, OnInit } from '@angular/core';
import { CommentService } from '../services/comment.service';
import { Comment } from '../models/comment.model';

@Component({
	selector: 'app-comment',
	template: `
		<div style="border: 1px solid #ccc; padding: 10px; margin: 10px 0;">
			<h4>Bình luận về Model</h4>
			<ul>
				<li *ngFor="let comment of comments">
					<strong>{{ comment.author }}</strong>: {{ comment.content }}
				</li>
			</ul>
		</div>
	`
})
export class CommentComponent implements OnInit {
	comments: Comment[] = [];

	// Tiêm CommentService vào component 
	constructor(private commentService: CommentService) {}

	ngOnInit(): void {
		// Gọi hàm từ service để lấy dữ liệu 
		this.commentService.getComments().subscribe(data => {
			this.comments = data;
		});
	}
}